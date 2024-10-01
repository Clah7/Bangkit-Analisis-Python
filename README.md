## Setup Environment - Anaconda

1. Buat environment baru dan aktifkan:

    ```bash
    conda create --name main-ds python=3.9
    conda activate main-ds
    ```

2. Install seluruh library yang diperlukan:

    ```bash
    pip install -r requirements.txt
    ```

## Setup Environment - Shell/Terminal

1. Buat folder baru untuk proyek:

    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    ```

2. Install dependencies menggunakan `pipenv`:

    ```bash
    pipenv install
    pipenv shell
    ```

3. Install library yang dibutuhkan:

    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi Streamlit

Setelah environment berhasil disiapkan, jalankan aplikasi dashboard Streamlit dengan perintah berikut:

```bash
streamlit run dashboard/dashboard.py