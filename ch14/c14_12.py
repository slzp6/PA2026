"""c14_12.py"""

# pylint: disable=pointless-string-statement

print("""
Python 3.12 では、Matplotlib の日本語表示に使われてきた
japanize-matplotlib が動作しません。内部で依存していた
distutils が削除されたためで、インポート時にエラーが発
生します。

その代わりとして、matplotlib-fontja が有効です。Python
3.12 に対応しており、読み込むだけで日本語フォントが自
動設定されるため、もっとも手軽に利用できます。

また、Noto Sans JP などのフォントを直接指定する方法も
確実で、seaborn や rcParams に設定を上書きされる問題を
避けられます。
""")


'''
# ==========
# Example of using matplotlib_fontja
# !pip install matplotlib-fontja
# 
import matplotlib_fontja
import matplotlib.pyplot as plt

plt.plot([8, 4, 3, 2, 1])
plt.xlabel("x軸")
plt.ylabel("y軸")
plt.title("日本語のタイトル")
# plt.show()
plt.savefig("c14_12.png")

'''

'''
# ========== 
# Example of using Noto Sans JP with mplfonts
# !pip install matplotlib 
# !pip install fonttools
# !pip install mplfonts
#
import matplotlib.pyplot as plt
from matplotlib import font_manager
import mplfonts

mplfonts.use_font("Noto Sans JP")
plt.rcParams["font.family"] = "Noto Sans JP"
plt.plot([8, 4, 3, 2, 1])
plt.xlabel("x軸")
plt.ylabel("y軸")
plt.title("日本語のタイトル")
# plt.show()
plt.savefig("c14_12.png")
'''

'''
# ==========
# Example of using japanize_matplotlib
# !pip install japanize-matplotlib
# 
import japanize_matplotlib
import matplotlib.pyplot as plt

plt.plot([8, 4, 3, 2, 1])
plt.xlabel("x軸")
plt.ylabel("y軸")
plt.title("日本語のタイトル")
# plt.show()
plt.savefig("c14_12.png")

'''
