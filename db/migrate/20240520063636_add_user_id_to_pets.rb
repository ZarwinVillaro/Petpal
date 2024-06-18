class AddUserIdToPets < ActiveRecord::Migration[7.1]
  def change
    add_column :pets, :user_id, :integer
    add_reference :pets, :user, foreign_key: true
  end
end
