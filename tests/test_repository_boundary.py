from __future__ import annotations

import os
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Source bytes, captures, transcripts, and renders never enter this repository.
MEDIA_SUFFIXES = {
    ".mp4", ".mov", ".mkv", ".avi", ".webm", ".wav", ".mp3", ".m4a", ".flac",
    ".pdf", ".docx", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".srt", ".vtt",
    ".zip",
}
SIZE_LIMIT_BYTES = 256 * 1024


def tracked_files() -> list[Path]:
    try:
        output = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z"],
            text=True, capture_output=True, check=True,
        ).stdout
        return [ROOT / name for name in output.split("\0") if name]
    except (OSError, subprocess.CalledProcessError):
        files: list[Path] = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if d not in {".git", "__pycache__"}]
            files.extend(Path(dirpath) / f for f in filenames)
        return files


class RepositoryBoundaryTest(unittest.TestCase):
    def test_no_media_or_capture_file_is_tracked(self) -> None:
        offenders = sorted(str(p.relative_to(ROOT)) for p in tracked_files() if p.suffix.lower() in MEDIA_SUFFIXES)
        self.assertEqual(offenders, [], f"media or capture files tracked: {offenders}")

    def test_no_tracked_file_exceeds_size_limit(self) -> None:
        offenders = sorted(
            f"{p.relative_to(ROOT)} ({p.stat().st_size} bytes)"
            for p in tracked_files() if p.is_file() and p.stat().st_size > SIZE_LIMIT_BYTES
        )
        self.assertEqual(offenders, [], f"oversized files tracked; study bytes belong in the external vault: {offenders}")

    def test_vault_root_pointer_is_not_tracked(self) -> None:
        names = {p.name for p in tracked_files()}
        self.assertNotIn(".vault-root", names)
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        self.assertIn(".vault-root", gitignore)


if __name__ == "__main__":
    unittest.main()
