class CreateAdoptions < ActiveRecord::Migration[7.1]
  def change
    create_table :adoptions do |t|
      t.string :full_name
      t.string :address
      t.string :contact
      t.text :reason

      t.timestamps
    end
  end
end
