import random


#  Creating mock participants
# PoW miners have a computational 'power'
miners = [
    {"name": "MinerA", "power": random.randint(1, 100)},
    {"name": "MinerB", "power": random.randint(1, 100)},
    {"name": "MinerC", "power": random.randint(1, 100)},
]

# PoS stakers have a locked-up 'stake' amount
stakers = [
    {"name": "StakerX", "stake": random.randint(1, 1000)},
    {"name": "StakerY", "stake": random.randint(1, 1000)},
    {"name": "StakerZ", "stake": random.randint(1, 1000)},
]

# DPoS delegates and votes from 3 mock voters
delegates = ["Del1", "Del2", "Del3"]
voters = ["Voter1", "Voter2", "Voter3"]
# Each voter randomly votes for one delegate
votes = [random.choice(delegates) for _ in voters]


# Step 2: Simulating Proof-of-Work
pow_winner = max(miners, key=lambda m: m["power"])
print("=== Proof-of-Work (PoW) ===")
for m in miners:
    print(f"  {m['name']} power: {m['power']}")
print(f"Selected miner: {pow_winner['name']} (highest power)\n")


#  Simulating Proof-of-Stake
pos_winner = max(stakers, key=lambda s: s["stake"])
print("=== Proof-of-Stake (PoS) ===")
for s in stakers:
    print(f"  {s['name']} stake: {s['stake']}")
print(f"Selected staker: {pos_winner['name']} (highest stake)\n")


#: Simulating  Delegated Proof-of-Stake
# Tally votes per delegate
vote_counts = {d: votes.count(d) for d in delegates}
print("=== Delegated Proof-of-Stake (DPoS) ===")
for voter, choice in zip(voters, votes):
    print(f"  {voter} voted for {choice}")
print("Vote tally:")
for d, count in vote_counts.items():
    print(f"  {d}: {count} votes")
# Select delegate with most votes (break ties randomly)
max_votes = max(vote_counts.values())
top_delegates = [d for d, c in vote_counts.items() if c == max_votes]
dpos_winner = random.choice(top_delegates)
print(f"Selected delegate: {dpos_winner} (highest votes)\n")

#  Displaying the consensus results
print("=== Consensus Summary ===")
print(f"PoW   winner: {pow_winner['name']}  (power = {pow_winner['power']})")
print(f"PoS   winner: {pos_winner['name']}  (stake = {pos_winner['stake']})")
print(f"DPoS  winner: {dpos_winner}         (votes = {vote_counts[dpos_winner]})")