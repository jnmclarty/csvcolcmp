# CSV Column Compare

Lists the elements of one column (left), which are not in another (right), across two CSVs

* Pure Python (s/b 2.7, +3.5)
* Column or 0-index based header selection
* Easy to tweak the reader or it's options (delimiter, escape, etc.)
* Ignores case and padding (via `.lower()` and `.strip()`)
* Single File
* In-RAM

... and no testing, license or warranty of any kind!

# Usage

```
wget http://github.com/jnmclarty/csvcolcmp
python main.py left.csv some_col right.csv other_col > left_not_in_right.csv
```