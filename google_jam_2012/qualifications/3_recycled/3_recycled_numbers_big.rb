require 'set'

def rotations(str)
  (1...str.length).collect { |i| (str * 2)[i, str.length] }
end

def trailing_zero(v)
  if v[0] == "0"
    true
  else
    false
  end
end

def collect_rotate(a, limit, set)
  astr = a.to_s
  digits = limit.to_s.length
  return if astr.length != digits
  rotations(astr).each do |v|
    if trailing_zero(v) || 
       v.to_i >= limit ||
       v.to_i <= a
      next
    else
      #print [a.to_i,v.to_i].sort
      #print "\n"
      set << [a, v.to_i].sort
    end
  end
end

def cache(key, map, &block) 
  map[key] = yield unless map[key]
  map[key]
end 

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
    collect_rotate(v, b, set)
  end

  puts "Case ##{count}: #{set.length}"
  count += 1
  #set.to_a.sort.each do |e|
  #  puts "#{e[0]} : #{e[1]}"
  #end
end

