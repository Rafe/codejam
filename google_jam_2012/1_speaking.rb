def get_map(clear_text, cipher, map = {})
  
  clear_text.length.times do |i|
    map[clear_text[i]] = cipher[i]
  end

  map_left = []
  char_left = %(abcdefghijklmnopqrstuvwxyz)
  %(abcdefghijklmnopqrstuvwxyz).each_char do |c|
    if map.has_key?(c)
      char_left.delete!(c)
    else
      map_left << c
    end
  end

  if map_left.length == 1 and char_left.length == 1
    map[map_left[0]] = char_left[0] 
  end

  if map_left.length == 2 and char_left.length == 2
    if map_left[0] == char_left[0]
      map[map_left[0]] = char_left[1]
      map[map_left[1]] = char_left[0]
    else
      map[map_left[0]] = char_left[0]
      map[map_left[1]] = char_left[1]
    end
  end
  map
end

def translate(text, map)
  result = ""
  text.each_char do |c|
    result << map[c] if map[c]
  end
  result
end

sample = <<-TEXT
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
TEXT

sample_result = <<-TEXT
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
TEXT

map = get_map(sample, sample_result)

count = 0
ARGF.readlines.each do |line|
  puts "Case ##{count}: "+ translate(line, map) unless count == 0
  count += 1
end
