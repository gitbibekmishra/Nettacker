from collections import Counter

import pytest

from tests.common import TestCase


class TestPasswords(TestCase):
    top_1000_common_passwords_path = (
        "lib/payloads/passwords/top_1000_common_passwords.txt"
    )

    def test_top_1000_common_passwords(self):
        with open(
            self.nettacker_path / self.top_1000_common_passwords_path
        ) as top_1000_file:
            # Filter out blank lines while reading the file
            top_1000_passwords = [
                line.strip() for line in top_1000_file.readlines() if line.strip()
            ]

        # Assert the total number of passwords is exactly 1000
        self.assertEqual(
            len(top_1000_passwords), 1000, "There should be exactly 1000 passwords"
        )

        # Assert all passwords are unique
        self.assertEqual(
            len(set(top_1000_passwords)),
            len(top_1000_passwords),
            f"The passwords aren't unique: {Counter(top_1000_passwords).most_common(1)[0][0]}",
        )