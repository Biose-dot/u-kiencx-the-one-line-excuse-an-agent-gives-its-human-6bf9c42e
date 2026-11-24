import os

ENTRY = "Sorry \u2014 I handed your deadline to a sub-agent, who handed it to another one, and now we are all in a meeting deciding whose fault it is."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
