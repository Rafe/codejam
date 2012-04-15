require 'set'

def is_rotate(a, b)
  return false if a.length != b.length || a.length <= 1
  return false if hash_pair(a) != hash_pair(b)
  digits = a.length
  shift = 0
  while(shift < digits)
    i = 0
    while(a[i] == b[(i + shift) % digits])
      i += 1
      return true if i == digits
    end
    shift += 1
  end
  false
end

def hash_pair(n)
  h = 0
  n.each_byte do |b|
    h += b
  end
  h
end

def cache(key, map, &block) 
  map[key] = yield unless map[key]
  map[key]
end 


a = 1000000
b = 2000000

count = 0
ARGF.readlines.each do |line|
  if count == 0
    count += 1
    next
  end

  set = Set.new

  args = line.split
  a = args.shift.to_i
  b = args.shift.to_i

  (a..b).each do |v|
    (v+1..b).each do |v2|
      if set.include?([v, v2])
        next
      elsif is_rotate(v.to_s, v2.to_s)
        set << [v, v2]
      end
    end
  end

  puts "Case ##{count}: #{set.length}"
  count += 1
  set.to_a.sort.each do |e|
    puts "#{e[0]} : #{e[1]}"
  end
end

