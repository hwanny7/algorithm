func solution(_ n:Int) -> String {
    let string:String = String(repeating:"수박", count: n / 2)
    return n % 2 == 0 ? string : string + "수"
}
