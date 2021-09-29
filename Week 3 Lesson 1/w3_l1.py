"""
Problem: explore linear regression tools in numpy, scipy, and pandas.

Author: Capt Stephen Stumpf
Date: 2021
Inputs: no command-line inputs, but appropriately-named files must be present in
the directory from which the script is executed.
Outputs: no return-value outputs, but the script will generate plots in new windows.
"""

# Python 101: Homework
## By Evelyn J. Boettcher
## Week 3 Lesson 1: Linear Regression

### Problem 1
### Explain what np.polynomial does in this script. 
### And what are my options besides Polynomial
if __name__=="__main__":
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv('co2_weekly_mlo.txt', skiprows=49, names=['yr', 'mon', 'day', 'decimal', 'ppm', ' #days', '1 yr ago','10 yr ago', 'since 1800'], delim_whitespace=True)
    clean_df = df[df.ppm != -999.99]
    pp = np.polynomial.Polynomial(np.polyfit(clean_df.decimal, clean_df.ppm, 3))
    plt.scatter(clean_df.decimal, clean_df.ppm)
    plt.plot(clean_df.decimal, pp(clean_df.decimal), color='red')
    plt.show()
### In the above code snippet, np.polynomial.Polynomial attempts to fit a polynomial line to the data contained in
### "clean_df.decimal" and "clean_df.ppm".  In the particular case, it attempts to fit a polynomial of degree 1,
### though other degrees are available. Other options are also available, including the methods Chebyshev, Hermite,
### HermiteE, Laguerre, and Legendre; each of these methods presents a convenient method for analysts to use that
### specific type of series.
### 
### Problem 2
    print(pp)
### print(pp) prints, in human-readable format, the polynomial contained in the pp data structure.
### Problem 3

### - [ ] What happens if you try to run this

#    import scipy as sp
#    sp.stats.linregress(clean_df.decimal, clean_df.ppm)
### I changed scipi to scipy; afterward, I receive the error "module 'scipy' has no attribute 'stats'".  We would be
### better served doing:
    from scipy import stats as stats
    results = stats.linregress(clean_df.decimal, clean_df.ppm)
    print(results)
### This code produces the following output:
###     LinregressResult(slope=1.8047605495309722, intercept=-3237.5569582578814, rvalue=0.9911821949894737,
###     pvalue=0.0, stderr=0.004878357419459059, intercept_stderr=9.747602868361888)
### This is far more helpful.

### Problem 4

###- [ ] For the Seaborn example 
###- [ ] Change the order to: 2 or 3

    import seaborn as sns; sns.set_theme(color_codes=True)
    ### import pandas as pd
    import matplotlib.pyplot as plt

# Get Data
    df = pd.read_csv('co2_weekly_mlo.txt', skiprows=49, names=['yr', 'mon', 'day', 'decimal','ppm', '#days', '1 yr ago', '10 yr ago', 'since 1800'], delim_whitespace=True)
    clean_df = df[df.ppm != -999.99]
# Set the plots
    ax = sns.regplot(x='decimal', y='ppm', data=clean_df, ci=95, order=3, line_kws={'label': 'Cubic regression line: $Y(X)=-1.8 X + 3498 X^2 - 2313807 X^3$', 'color': 'm'}, label="CO2 Weekly average")
    ax.set_ylabel("CO2 (ppm)")
    ax.set_xlabel("Year")
    ax.legend(loc="upper left")
    plt.show()

### Problem 5 (a,b)
###   - [ ] Add x_bins = 100
###     ax = sns.regplot(x='decimal', y='ppm', data=clean_df, x_bins=100, ci=95, order=3, line_kws={'label': 'Cubic regression line: $Y(X)=-1.8 X + 3498 X^2 - 2313807 X^3$', 'color': 'm'}, label="CO2 Weekly average")
###   - [ ] Add x_bins = 50
###     ax = sns.regplot(x='decimal', y='ppm', data=clean_df, x_bins=50, ci=95, order=3, line_kws={'label': 'Cubic regression line: $Y(X)=-1.8 X + 3498 X^2 - 2313807 X^3$', 'color': 'm'}, label="CO2 Weekly average")
### Each of these commands bins the data into discrete chunks of the given number.  The result is a graph that looks "cleaner"
### to the eye, and presents less visual noise to the user.  The reader should be informed of this, though, to prevent
### misinterpretation.

