import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var new_list: [Int] = num_list
    let last: Int = num_list.last!
    let next: Int = num_list[num_list.count - 2]
    new_list.append(last > next ? last - next : last * 2)
    
    return new_list
}
