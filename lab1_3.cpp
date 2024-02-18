#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::vector<int> ReadKey(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<int> key;

    if (!file.is_open()) {
        std::cerr << "Error opening key file." << std::endl;
        return key;
    }

    int num;
    while (file >> num) {
        key.push_back(num);
    }

    file.close();

    return key;
}

void PadFile(std::string& data) {
    while (data.size() % 5 != 0) {
        data += 'z';
    }
}

std::string Encrypt(const std::string& data, const std::vector<int>& key) {
    std::string result = "";
    int columns = 5;
    int rows = data.size() / columns;
    for (int row = 0; row < rows; ++row) {
        for (int col : key) {
            result += data[col + row * columns];
        }
    }

    return result;
}


std::string Decrypt(const std::string& data, const std::vector<int>& key) {
    std::string result = "";
    int columns = 5;
    int rows = data.size() / key.size();
    std::vector<int> inv_key(key.size());
    for (int i = 0; i < key.size(); ++i) {
        inv_key[key[i]] = i;
    }
    for (int row = 0; row < rows; ++row) {
        for (int col : inv_key) {
            result += data[col + row * columns];
        }
    }

    return result;
}


int main() {
    std::vector<int> key = ReadKey("key.txt");

    std::ifstream file("input.txt");
    if (!file.is_open()) {
        std::cerr << "Error opening input file." << std::endl;
        return 1;
    }

    std::string data((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    PadFile(data);

    char mode;
    std::cout << "Enter 'e' for encryption or 'd' for decryption: ";
    std::cin >> mode;

    if (mode == 'e') {
        std::string encrypted_data = Encrypt(data, key);
        std::ofstream output_file("output.txt");
        output_file << encrypted_data;
        output_file.close();
        std::cout << "Encryption completed. Encrypted data saved to 'output.txt'\n";
    }
    else if (mode == 'd') {
        std::string decrypted_data = Decrypt(data, key);
        std::ofstream output_file("output.txt");
        output_file << decrypted_data;
        output_file.close();
        std::cout << "Decryption completed. Decrypted data saved to 'output.txt'\n";
    }
    else {
        std::cout << "Invalid mode. Please enter 'e' or 'd'.\n";
    }

    return 0;
}
