import hashlib
from datetime import datetime, timezone
import time  # for measuring elapsed time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp              
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Returns the SHA-256 hash of the block contents, including nonce.
        """
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Increments nonce until block hash starts with '0' * difficulty.
        Returns the number of attempts and elapsed time.
        """
        target = "0" * difficulty
        start_time = time.time()
        attempts = 0

        # Loop until Hash == '0' * difficulty   
        while True:
            self.hash = self.calculate_hash()
            attempts += 1
            if self.hash.startswith(target):
                break
            self.nonce += 1

        elapsed = time.time() - start_time
        return attempts, elapsed

    def __str__(self):
        return (
            f"Block {self.index} [\n"
            f"  Timestamp : {self.timestamp.isoformat()}\n"
            f"  Data      : {self.data}\n"
            f"  Prev Hash : {self.previous_hash}\n"
            f"  Nonce     : {self.nonce}\n"
            f"  Hash      : {self.hash}\n"
            "]"
        )

genesis = Block(
    index=0,
    timestamp=datetime.now(timezone.utc),
    data="Genesis Block",
    previous_hash="0"
)
print("=== Genesis Block ===")
print(genesis)
print()

new_block = Block(
    index=1,
    timestamp=datetime.now(timezone.utc),
    data="Alice → Bob: 20 BTC",
    previous_hash=genesis.hash
)

#  Mining  the block with specified difficulty

difficulty = 4
print(f"Mining block with difficulty = {difficulty} (hash prefix '{'0'*difficulty}')...")
attempts, elapsed = new_block.mine_block(difficulty)


# Mining results and the mined block
print(f"Done! Nonce found: {new_block.nonce}")
print(f"Hash: {new_block.hash}")
print(f"Total attempts: {attempts}")
print(f"Elapsed time: {elapsed:.4f} seconds\n")

print("=== Mined Block ===")
print(new_block)