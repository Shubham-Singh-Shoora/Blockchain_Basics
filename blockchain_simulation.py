import hashlib  # Import hashlib for SHA-256 hashing
from datetime import datetime, timezone

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                # Position of the block in the chain
        self.timestamp = timestamp        # When the block was created
        self.data = data                  # Payload (e.g., a list of transactions)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = 0                    # Arbitrary number (will stay 0 here)
        self.hash = self.calculate_hash() # Hash of this block

    def calculate_hash(self):
        """
        Calculate SHA-256 over the concatenation of:
        index, timestamp, data, previous_hash, nonce
        """
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return (
            f"Block {self.index} [\n"
            f"  Timestamp    : {self.timestamp}\n"
            f"  Data         : {self.data}\n"
            f"  Previous Hash: {self.previous_hash}\n"
            f"  Hash         : {self.hash}\n"
            f"  Nonce        : {self.nonce}\n"
            "]"
        )


#Create and link 3 blocks
# Genesis Block
genesis_block = Block(
    index=0,
    timestamp=datetime.now(timezone.utc),
    data="Genesis Block",
    previous_hash="0"
)

# Block 1 
block1 = Block(
    index=1,
    timestamp=datetime.now(timezone.utc),
    data="Shubham → Anshul: 10 BTC",
    previous_hash=genesis_block.hash
)

# Block 2 
block2 = Block(
    index=2,
    timestamp=datetime.now(timezone.utc),
    data="Mansi → Parag: 5 BTC",
    previous_hash=block1.hash
)

# Chain list will be this
blockchain = [genesis_block, block1, block2]


#Display the blockchain
print("=== Original Blockchain ===")
for blk in blockchain:
    print(blk)
    print()

# ------------------------------------------------------------------------------
#Tamper with Block 1’s data and recalculate its hash
print(">>> Tampering with Block 1's data...")


block1.data = "Shubham → Anshul: 100 BTC" # Change the data in Block 1 for tampering
# Recompute its hash
block1.hash = block1.calculate_hash()

# Now Block 2’s previous_hash no longer matches block1.hash
print("\n=== Blockchain After Tampering ===")
for blk in blockchain:
    print(blk)
    print()

print(">>> Checking integrity:")
for i in range(1, len(blockchain)):
    current = blockchain[i]
    prev = blockchain[i - 1]
    valid_link = (current.previous_hash == prev.hash)
    status = "OK" if valid_link else "BROKEN"
    print(f"Block {current.index} link to Block {prev.index}: {status}")