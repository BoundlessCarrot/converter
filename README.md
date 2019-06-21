# Converter

Convert between the 2 common temperature scales quickly and easily from the command line

## Installation
Just clone the repo

```git clone https://github.com/BoundlessCarrot/converter.git```

and add the respective aliases to your bash profile. For example, my aliases look like this:

```
alias ftoc='python3 ~/converter/ftoc.py'
alias ctof='python3 ~/converter/ctof.py'
```

NOTE: In the alias, do not add a space after the last character. The scripts will not work if you do. (```ftoc``` 👍🏽 ```ftoc ```  👎🏽)

## Usage

Really, it's as simple as:

```<ALIAS> <VALUE>```

So for my aliases, converting 23 celsius to farenheit looks like this:

```ctof 23```

__That's it__

## Extras

In the future, I'd like to add:
  - More conversions
  - Maybe converge all conversions into one file?
  - Automagically do the bash profile stuff (or get rid of it completely, who knows)

That's pretty much it. Happy converting!
