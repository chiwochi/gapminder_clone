# Hans Rosling's 200 countries, 200 Years, 4 Minutes

## 簡介

復刻[Hans Rosling's 200 countries, 200 Years, 4 Minutes](https://youtu.be/jbkSRLYSojo?si=5WkjOoiU_IPuKGsR)
使用了 `pandas` & `sqlite3` 建立資料庫，利用 `matplotlib` 進行概念驗證，最後以 `plotly.express` 做出成品。

## 如何重現

- 安裝 [Miniconda](https://docs.anaconda.com/miniconda)
- 依據 `environment.yml` 建立環境

```bash
conda env create -f environment.yml`
```

- 將 `data/` 資料夾中的四個CSV檔案放在工作目錄中的 `data/` 資料夾
- 啟動環境並執行 `python create_gapminder_db.py` 就能在 `data/` 資料夾中建立 `gapminder.db`
- 啟動環境並執行 `python plot_with_px.py` 就能生成 `gapminder_clone.html` 