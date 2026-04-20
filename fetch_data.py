import yfinance as yf
import pandas as pd

def veri_cek_bist(sembol, baslangic="2010-01-01", bitis="2025-01-01"):
    """
    BIST hisse verilerini güvenli bir şekilde çeker.
    Örnek sembol: 'THYAO.IS', 'ASELS.IS' (BIST için sonuna .IS eklenmeli)
    """
    ticker_name = f"{sembol}.IS"
    print(f"--- {ticker_name} verisi indiriliyor... ---")
    
    try:
        # Ticker nesnesini oluştur ve veriyi çek
        ticker = yf.Ticker(ticker_name)
        df = ticker.history(start=baslangic, end=bitis, interval="1d")
        
        if df.empty:
            print("Veri bulunamadı. Lütfen sembolü veya tarih aralığını kontrol edin.")
            return None
        
        # Ödevde istenen zorunlu sütunları filtrele 
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
        
        # Tarih index'ini temizle (Borsa kapalı günler çıkarılmış olur) 
        df.index = pd.to_datetime(df.index).date
        
        print(f"Başarıyla {len(df)} satır veri çekildi.")
        return df

    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

# Kullanım Örneği:
# Ödev kriteri: 10M TL hacim üstü ve 15 yıllık geçmiş [cite: 12, 13]
hisse_df = veri_cek_bist("THYAO") 

CSV_PATH = "thyao_veri.csv"

if hisse_df is not None:
    print(hisse_df.head())
    hisse_df.to_csv(CSV_PATH)
    print(f"✅ Veri kaydedildi: {CSV_PATH}")

# ── Kayıtlı veriyi yüklemek için ──────────────────────────────────────────
# Veriyi tekrar çekmek zorunda kalmadan buradan devam edebilirsin:
# hisse_df = pd.read_csv(CSV_PATH, index_col=0, parse_dates=True)