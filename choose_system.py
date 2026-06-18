#!/usr/bin/env python3
import platform
import sys

def main():
    name = "Чекунов Анзор"
    system = platform.system()
    version = platform.version()
    
    print(f"Name: {name}")
    print(f"System: {system}")
    print(f"Version: {version}")
    
    if system == "Linux":
        if "Ubuntu" in version or "Debian" in version:
            print("Recommended: apt-get (Ubuntu/Debian)")
            print("Packages: texlive-latex-recommended, texlive-fonts-recommended, texlive-latex-extra, texlive-fonts-extra, texlive-lang-cyrillic, texlive-generic-recommended, texlive-pictures, texlive-science, cm-super, dvipng")
        elif "Fedora" in version or "RedHat" in version:
            print("Recommended: yum (Fedora/RedHat)")
            print("Packages: texlive-collection-latexrecommended, texlive-collection-fontsrecommended, texlive-collection-pictures, texlive-collection-science, texlive-collection-langcyrillic")
        else:
            print("Unknown Linux distribution")
    elif system == "Windows":
        print("Recommended: Use Docker on Windows with Ubuntu base image")
    elif system == "Darwin":
        print("Recommended: Use Docker on macOS with Ubuntu base image")
    else:
        print(f"Unsupported system: {system}")

if __name__ == "__main__":
    main()