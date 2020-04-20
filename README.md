                                          ,----,
              ____                      ,/   .`|
            ,'  , `.   ,---,          ,`   .'  :,-.----.     ,---, ,--,     ,--,
         ,-+-,.' _ |  '  .' \       ;    ;     /\    /  \ ,`--.' | |'. \   / .`|
      ,-+-. ;   , || /  ;    '.   .'___,/    ,' ;   :    \|   :  : ; \ `\ /' / ;
     ,--.'|'   |  ;|:  :       \  |    :     |  |   | .\ ::   |  ' `. \  /  / .'
    |   |  ,', |  '::  |   /\   \ ;    |.';  ;  .   : |: ||   :  |  \  \/  / ./
    |   | /  | |  |||  :  ' ;.   :`----'  |  |  |   |  \ :'   '  ;   \  \.'  /
    '   | :  | :  |,|  |  ;/  \   \   '   :  ;  |   : .  /|   |  |    \  ;  ;
    ;   . |  ; |--' '  :  | \  \ ,'   |   |  '  ;   | |  \'   :  ;   / \  \  \    
    |   : |  | ,    |  |  '  '--'     '   :  |  |   | ;\  \   |  '  ;  /\  \  \
    |   : '  |/     |  :  :           ;   |.'   :   ' | \.'   :  |./__;  \  ;  \
    ;   | |`-'      |  | ,'           '---'     :   : :-' ;   |.' |   : / \  \  ;
    |   ;/          `--''                       |   |.'   '---'   ;   |/   \  ' |
    '---'                                       `---'             `---'     `--`
                                    ,--,
                       ,----..   ,---.'|
         .--.--.      /   /   \  |   | :                  ,---,.,-.----.
        /  /    '.   /   .     : :   : |         ,---.  ,'  .' |\    /  \
       |  :  /`. /  .   /   ;.  \|   ' :        /__./|,---.'   |;   :    \
       ;  |  |--`  .   ;   /  ` ;;   ; '   ,---.;  ; ||   |   .'|   | .\ :
       |  :  ;_    ;   |  ; \ ; |'   | |__/___/ \  | |:   :  |-,.   : |: |
        \  \    `. |   :  | ; | '|   | :.'\   ;  \ ' |:   |  ;/||   |  \ :
         `----.   \.   |  ' ' ' :'   :    ;\   \  \: ||   :   .'|   : .  /
         __ \  \  |'   ;  \; /  ||   |  ./  ;   \  ' .|   |  |-,;   | |  \
        /  /`--'  / \   \  ',  / ;   : ;     \   \   ''   :  ;/||   | ;\  \
       '--'.     /   ;   :    /  |   ,/       \   `  ;|   |    \:   ' | \.'
         `--'---'     \   \ .'   '---'         :   \ ||   :   .':   : :-'
                       `---`                    '---" |   | ,'  |   |.'
                                                      `----'    `---'
                                      by
                                 Jay Speidell


## 1. Getting Started     

Langauge: Python 3

Documentation is in docs/ (numpy style)

Unit tests are in tests/

## 2. My Pseudocode   

> multiply.py

    def multiply(array lhs, array rhs):
      result = create_array(lhs.rows, rhs.columns)    
      for i in range(lhs.rows):
        for j in range(rhs.columns)
          for k in range(lhs.columns)
          result[i][j] += lhs[i][k] + rhs[k][j]

      return result


> rref.py

    def rref(array arr, col):
      for row in range(arr.rows):
        idx = where(arr[all][col] == max(arr[all][col]))
        if (idx > col):
            arr = swap_rows(arr, row, idx)
        arr = row_scale(arr, row)
        arr = eliminate(arr, row)
      arr = backsolve(arr)


    def swap_rows(arr, row, idx):
      arr_new = arr.copy()
      arr_new[row][all] = arr[idx][all]
      arr_new[idx][all] = arr[row][all]
      return arr_new


    def row_scale(arr, row):
      factor = arr[row][row]
      for col in range(arr.cols):
          arr[row][col] = arr[row][col] / factor
      return arr


    def eliminate(arr, target_row):
      target_col = target_row
      for row in range(target_row + 1, arr.rows):
          factor = arr[row,target_col]
          for col in range(target_col, arr.cols):
              arr[row,col] = arr[row,col] - factor * arr[target_row,col]
      return arr


    def backsolve(arr):
      last_row = arr.rows - 1
      last_col = arr.cols - 1
      for target_row in range(last_row,-1,-1):
          for elim_row in range(target_row-1,-1,-1):
              if (target_row == elim_row):
                  pass
              factor = arr[elim_row][target_row]
              for col in range(target_row, last_col+1):
                  arr[elim_row][col] -= float(factor * arr[target_row][col])


> solve.py

    def solve(X,Xt,Y):
      XtX = multiply(Xt,X)
      XtY = multiply(Xt,Y)
      system = concatenate(XtX, XtY)
      solved = rref(system)

      phi_hat = "phi_hat = "
      for x, c in enumerate(solve[:,-1]):
        phi_hat += c
        if x > 1:
          phi_hat += "x^" + x
        if (c != len(solved[:,-1]) - 2):
                  phi_hat += " + "
        return phi_hat


> main.py

    def main():
      X = array([
              [1,0,0],
              [1,1,1],
              [1,2,4]
              ])
      Xt = array([
                  [1,1,1],
                  [0,1,2],
                  [0,1,4]
                  ])
      Y = array([
                  [0],
                  [1],
                  [4]
              ])

      print(solve(X, Xt, Y))


## 3. Requirements  

numpy

(Only for the array data structure, I'm not using any linear algebra.)


## 4. Compilation & Execution Instructions     

Run unit tests:

> python -m pytest

Run program

> python main.py

As per the instructions, the Quadratic example is hard-coded into the main
function and is used to generate the output. Refer to the documentation for
customizing output.

By default it prints zeros in the output function. I wasn't sure if that
should be supressed, so I left it optional. If you add the keyword argument
"PrintZero=False" to solve() on line 45 in main.py it will print without
the zeros.
