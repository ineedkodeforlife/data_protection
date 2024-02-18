#include <iostream>
#include <fstream>
#include <vector>

std::vector<size_t> CountBytesAppearing(const std::string& filename) {
    std::ifstream file(filename, std::ios::binary);

    if (!file.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return std::vector<size_t>(256, 0);
    }

    std::vector<size_t> bytes_appearing(256, 0);
    char byte;
    while (file.get(byte)) {
        ++bytes_appearing[static_cast<unsigned char>(byte)];
    }

    file.close();

    return bytes_appearing;
}

void CoutBytesAppearing(const std::vector<size_t>& bytes_appearing) {
    for (size_t byte = 0; byte < bytes_appearing.size(); ++byte) {
        if (bytes_appearing[byte] > 0) {
            std::cout << "[" << byte << " ] = " << bytes_appearing[byte] << '\n';
        }
    }
}


int main() {
    std::string filename = "C:\\Users\\vitrl\\OneDrive\\Рабочий стол\\lab_1_test.docx";
    CoutBytesAppearing(CountBytesAppearing(filename));
    std::ifstream file(filename, std::ios::binary | std::ios::ate);
    std::streampos fileSize = file.tellg();
    file.close();

    std::cout << "File size in bytes: " << fileSize << std::endl;


    return 0;
}