fname = input("Enter the file name: ")
try:
    fhand = open(fname, "r")
    total_conf = 0.0
    count = 0

    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            conf_str = line.split(":")[1].strip()
            try:
                confidence = float(conf_str)
                total_conf += confidence
                count += 1
            except ValueError:
                continue

    if count > 0:
        average_conf = total_conf / count
        print(f"Average spam confidence: {average_conf:.14f}")
    else:
        print("No X-DSPAM-Confidence lines found in the file")
    
    fhand.close()
except FileNotFoundError:
    print(f"File cannot be opened: {fname}")


