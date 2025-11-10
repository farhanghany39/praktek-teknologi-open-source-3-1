import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions  # bisa berupa list transaksi
        self.timestamp = timestamp or time.time()
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Menghitung hash SHA-256 dari isi blok"""
        # Menggunakan json.dumps untuk konsistensi string dari transactions
        block_string = f"{self.index}{self.previous_hash}{json.dumps(self.transactions, sort_keys=True)}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """Melakukan Proof-Of-Work sederhana:
        mencari hash yang diawali dengan sejumlah '0' sesuai difficulty
        """
        print(f"Mining block {self.index}...")
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined! Hash: {self.hash}\n")

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []
        self.mining_reward = 50  # contoh reward

    def create_genesis_block(self):
        """Blok pertama dalam blockchain"""
        return Block(0, "0", ["Genesis Block"])

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        """Menambahkan transaksi baru"""
        transaction = {
            "from": sender,
            "to": receiver,
            "amount": amount
        }
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        """Menambang transaksi yang tertunda dan membuat blok baru"""
        if not self.pending_transactions:
            print("Tidak ada transaksi untuk ditambang.")
            return

        new_block = Block(
            index=len(self.chain),
            previous_hash=self.get_latest_block().hash,
            transactions=self.pending_transactions
        )

        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

        print(f"Miner {miner_address} menerima reward {self.mining_reward} coin\n")

        # reset transaksi tertunda dengan satu transaksi reward
        self.pending_transactions = [{
            "from": "Blockchain System",
            "to": miner_address,
            "amount": self.mining_reward
        }]

    def is_chain_valid(self):
        """Memeriksa integritas blockchain"""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # verifikasi hash
            if current.hash != current.calculate_hash():
                print("Hash tidak valid pada block", current.index)
                return False

            # verifikasi hubungan blok
            if current.previous_hash != previous.hash:
                print("Previous hash tidak cocok pada block", current.index)
                return False

        print("Blockchain valid")
        return True

    def print_chain(self):
        """Menampilkan seluruh blok"""
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Transactions: {block.transactions}")
            print(f"  Hash: {block.hash}")
            print(f"  Prev: {block.previous_hash}")
            print(f"  Nonce: {block.nonce}\n")

# Contoh penggunaan
if __name__ == "__main__":
    my_coin = Blockchain(difficulty=3)

    # Tambahkan beberapa transaksi
    my_coin.add_transaction("Alice", "Bob", 100)
    my_coin.add_transaction("Bob", "Charlie", 30)

    # Tambang transaksi
    my_coin.mine_pending_transactions("Miner1")

    # Tambahkan transaksi baru dan tambang lagi
    my_coin.add_transaction("Charlie", "Alice", 25)
    my_coin.mine_pending_transactions("Miner2")

    # Tampilkan isi blockchain
    my_coin.print_chain()

    # Cek validitas rantai
    my_coin.is_chain_valid()
