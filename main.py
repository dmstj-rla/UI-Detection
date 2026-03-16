from perception.ubuntu_ui_extractor import extract_ui_elements


def main():

    print("Extracting UI elements...\n")

    elements = extract_ui_elements()

    print("Total elements:", len(elements))
    print()

    for i, e in enumerate(elements):

        print(f"[{i}]")
        print("name:", e["name"])
        print("type:", e["control_type"])
        print("parent:", e["parent_name"])
        print("bbox:", e["bbox"])
        print("center:", e["center"])
        print()


if __name__ == "__main__":
    main()