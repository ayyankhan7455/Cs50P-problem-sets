def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                m, d, y = date.split("/")
                month, day, year = int(m), int(d), int(y)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            elif "," in date:
                month_day, y = date.split(",")
                year = int(y.strip())
                m_str, d_str = month_day.strip().split()
                day = int(d_str)
                m_title = m_str.title()
                if m_title in months and 1 <= day <= 31:
                    month = months.index(m_title) + 1
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
