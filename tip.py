def split(total, people, tip=0.1):
    return round(total * (1 + tip) / people, 2)

if __name__ == "__main__":
    print(split(120, 4))
