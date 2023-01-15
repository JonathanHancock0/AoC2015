if __name__ == '__main__':
    for n in range(1, 26):
        f = open(f"{n}.py", 'w')
        f.write("if __name__ == '__main__':")
        f.close()