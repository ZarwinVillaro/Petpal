class AddPetIdToAdoptions < ActiveRecord::Migration[7.1]
  def change
    add_reference :adoptions, :pet, null: false, foreign_key: true
  end
end
