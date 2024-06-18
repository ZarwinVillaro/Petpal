class CreateResources < ActiveRecord::Migration[7.1]
  def change
    create_table :resources do |t|
      t.string :rails
      t.string :generate
      t.string :scaffold
      t.string :Resource
      t.string :name
      t.text :description
      t.string :category
      t.string :url
      t.datetime :published_at

      t.timestamps
    end
  end
end
