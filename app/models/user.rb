class User < ApplicationRecord
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  has_one_attached :image
  has_many :pets, dependent: :destroy

  enum role: { user: 'user', admin: 'admin', pet_owner: 'pet_owner' }

  after_initialize :set_default_role, if: :new_record?

  def set_default_role
    self.role ||= 'user'
  end
end
