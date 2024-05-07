def section(txt):
    print(
        "\n╔══════════════════════════════════════════════════════════════════════════════╗"
    )
    str_upper = "║   " + txt.upper()
    n_str = len(str_upper)
    str_empty = " " * (79 - n_str)
    str_full = str_upper + str_empty + "║"
    print(str_full)
    print(
        "╚══════════════════════════════════════════════════════════════════════════════╝"
    )


def subsection(txt):
    print("\n┌────────────────────────────────────────┐")
    str_upper = "│   " + txt.upper()
    n_str = len(str_upper)
    str_empty = " " * (41 - n_str)
    str_full = str_upper + str_empty + "│"
    print(str_full)
    print("└────────────────────────────────────────┘")


def subsubsection(txt):
    print("\n─── {} ───".format(txt))
