func solution(_ phone_number:String) -> String {
    let firstIndex = phone_number.index(phone_number.startIndex, offsetBy: phone_number.count - 4)
    return String(repeating: "*", count: phone_number.count - 4) + String(phone_number[firstIndex...])
}
