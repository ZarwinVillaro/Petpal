class Pet < ApplicationRecord
    has_one_attached :image
    belongs_to :user
    validates :name, :age, :breed, :category, :description, presence: true

    CATEGORIES = ['Cat', 'Dog', 'Bird', 'Other']
    validates :category, inclusion: { in: CATEGORIES }
end
