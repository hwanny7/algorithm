import Foundation

func solution(_ s:String) -> Int {
    var index: Int = 0
    let stringArray: [String] = s.map{ String($0) }
    var ans: String = ""

    while index < s.count {
        let char: String = stringArray[index]

        if let intChar = Int(char) {
            index += 1
            ans += String(intChar)
            continue
        }

        switch char {
            case "z":
            index += 4
            ans += "0"
            case "o":
            index += 3
            ans += "1"
            case "e":
            index += 5
            ans += "8"
            case "n":
            index += 4
            ans += "9"

            case "t":
            if stringArray[index..<index + 3].joined() == "two" {
                index += 3
                ans += "2"
            } else {
                index += 5
                ans += "3"
            }

            case "f":
            if stringArray[index..<index + 4].joined() == "four" {
                index += 4
                ans += "4"
            } else {
                index += 4
                ans += "5"
            }
            case "s":
            if stringArray[index..<index + 3].joined() == "six" {
                index += 3
                ans += "6"
            } else {
                index += 5
                ans += "7"
            }
            default:
            print(char)

        }
    }


    return Int(ans)!
}
