playlist = []

while True:
    print("\nMENU QUẢN LÝ DANH SÁCH PHÁT")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và trích xuất danh sách")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case "1":
            print("\nTHÊM BÀI HÁT")
            print("1. Thêm vào cuối danh sách")
            print("2. Chèn vào vị trí cụ thể")

            sub_choice = input("Nhập lựa chọn: ")

            song_name = input("Nhập tên bài hát: ")

            match sub_choice:
                case "1":
                    playlist.append(song_name)
                    print("Thêm bài hát thành công!")
                    print("Số lượng bài hát hiện tại:", len(playlist))

                case "2":
                    index = input("Nhập vị trí muốn chèn: ")

                    if not index.isdigit():
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
                    else:
                        index = int(index)

                        if index < 1 or index > len(playlist) + 1:
                            print("Vị trí không hợp lệ.")
                        else:
                            playlist.insert(index - 1, song_name)
                            print("Thêm bài hát thành công!")
                            print("Số lượng bài hát hiện tại:", len(playlist))

                case _:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

        case "2":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\nDANH SÁCH PHÁT")

                for i in range(len(playlist)):
                    print(f"{i + 1}. {playlist[i]}")

                print("\nTổng số bài hát:", len(playlist))

        case "3":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\nXÓA BÀI HÁT")
                print("1. Xóa theo tên bài hát")
                print("2. Xóa theo số thứ tự")

                sub_choice = input("Nhập lựa chọn: ")

                if not sub_choice.isdigit():
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
                    continue

                match sub_choice:
                    case "1":
                        song_name = input("Nhập tên bài hát cần xóa: ")

                        if song_name in playlist:
                            playlist.remove(song_name)
                            print(f"Đã xóa bài hát {song_name} khỏi danh sách")
                        else:
                            print("Không tìm thấy bài hát trong danh sách phát.")

                    case "2":
                        position = input("Nhập số thứ tự cần xóa: ")

                        if not position.isdigit():
                            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
                        else:
                            position = int(position)

                            if position < 1 or position > len(playlist):
                                print("Vị trí không hợp lệ.")
                            else:
                                removed_song = playlist.pop(position - 1)
                                print(f"Đã xóa bài hát {removed_song} khỏi danh sách")

                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

        case "4":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\nSẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH")
                print("1. Sắp xếp danh sách phát theo bảng chữ cái A-Z")
                print("2. Hiển thị 3 bài hát đầu tiên")

                sub_choice = input("Nhập lựa chọn: ")

                if not sub_choice.isdigit():
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
                    continue

                match sub_choice:
                    case "1":
                        playlist.sort()

                        print("\nDanh sách sau khi sắp xếp:")

                        for i in range(len(playlist)):
                            print(f"{i + 1}. {playlist[i]}")

                    case "2":
                        print("\n3 bài hát đầu tiên:")

                        for i in range(min(3, len(playlist))):
                            print(f"{i + 1}. {playlist[i]}")

                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")

        case "5":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")