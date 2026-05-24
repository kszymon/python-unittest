import random
from unittest.mock import Mock, patch

for i in range(5):
    print(random.randint(1, 6))

print()

with patch('random.randint') as mock_random:
    mock_random.return_value = 5
    for i in range(5):
        print(random.randint(1, 6))

print()

for i in range(5):
    print(random.randint(1, 6))