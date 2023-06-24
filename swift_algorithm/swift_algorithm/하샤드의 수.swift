func solution(_ x:Int) -> Bool {
    
    var num: Int = x
    var sum: Int = 0
    
    while num > 0 {
        sum += num % 10
        num /= 10
    }
    
    return x % sum == 0 ? true : false
}
