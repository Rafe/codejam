module ActiveRecord
  class Base
    def self.has_many(name, options)
      p [name, options]
    end
  end
end

class User < ActiveRecord::Base
  has_many :roles, :dependent => :test
end
