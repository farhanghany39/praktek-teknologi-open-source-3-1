from flask import Flask, render_template, jsonify

app = Flask(__name__)

# --- JAWABAN SOAL NO 1 (WEBSITE) ---

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/harga')
def harga():
    list_harga = [
        {"paket": "Basic", "biaya": "Rp 50.000"},
        {"paket": "Pro", "biaya": "Rp 150.000"},
        {"paket": "Enterprise", "biaya": "Hubungi Kami"}
    ]
    return render_template('harga.html', data_harga=list_harga)

@app.route('/siswa')
def api_siswa():
    # Data sesuai dengan tabel di gambar soal
    data_siswa_tkj = [
        {
            "no": 1,
            "nama": "Ahmad Hasyim Arifin",
            "nis": "0001",
            "ttl": "Blora, 16-09-2001",
            "nama_ortu": "Nur Hasyim",
            "alamat": "Banjarejo"
        },
        {
            "no": 2,
            "nama": "Ahmad Koirul Amin",
            "nis": "0002",
            "ttl": "Blora, 25-08-2002",
            "nama_ortu": "Sugiyo",
            "alamat": "Kunduran"
        },
        {
            "no": 3,
            "nama": "Alvin Rahmad V",
            "nis": "0003",
            "ttl": "Bojonegoro, 01-06-2002",
            "nama_ortu": "Suwito",
            "alamat": "Tambakrejo"
        },
        {
            "no": 4,
            "nama": "Alvina Nur Santi",
            "nis": "0004",
            "ttl": "Blora, 21-10-2001",
            "nama_ortu": "Sanuri",
            "alamat": "Todanan"
        },
        {
            "no": 5,
            "nama": "Anggara Putra",
            "nis": "0005",
            "ttl": "Grobogan, 31-03-2002",
            "nama_ortu": "Saryono",
            "alamat": "Ngaringan"
        },
        {
            "no": 6,
            "nama": "Indah Astriana",
            "nis": "0006",
            "ttl": "Blora, 02-01-2002",
            "nama_ortu": "Sumito",
            "alamat": "Kunduran"
        }
    ]
    
    # jsonify mengubah list python di atas menjadi format JSON
    return jsonify(data_siswa_tkj)

if __name__ == '__main__':
    app.run(debug=True)