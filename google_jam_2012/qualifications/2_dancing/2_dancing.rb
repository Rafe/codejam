def max_score(num)
  return [0, 0] if num == 0
  avg = num / 3
  residual = num % 3
  case residual
  when 0
    [avg, avg + 1]
  when 1
    [avg + 1, avg + 1]
  when 2
    [avg + 1, avg + 2]
  end
end

def cache(key, map = {}, &block)
  map[key] = yield if not map[key]
  map[key]
end

map = {}
ARGF.readlines.each_with_index do |line, count|
  next if count == 0
  
  args = line.split
  n = args.shift

  s = args.shift.to_i
  point = args.shift.to_i

  over = 0
  need_star = 0
  args.each do |t|
    score = cache(t, map) { max_score(t.to_i) }
    if score[0] >= point
      over += 1
    elsif score[1] >= point 
      need_star += 1
    end
  end

  over += [need_star, s].min

  puts "Case ##{count}: #{over}"
end
