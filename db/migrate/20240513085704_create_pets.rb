class CreatePets < ActiveRecord::Migration[7.1]
  def change
    create_table :pets do |t|
      t.string :name
      t.integer :age
      t.string :breed
      t.text :description

      t.timestamps
    end
  end
end
