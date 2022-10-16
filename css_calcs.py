base_size = 16
scale_ratio = 1.33

def get_scale_values(base_size, scale_ratio):
    vals = []
    x = base_size
    for i in range(6):
        vals.append(round(x*scale_ratio, 3))
        x *= scale_ratio
    return vals

def main():
    vals = get_scale_values(base_size, scale_ratio)
    print(vals)
    
if __name__ == "__main__":
    main()