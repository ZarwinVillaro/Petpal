class AddPetOwnerAndChangeRoleToStringInUsers < ActiveRecord::Migration[7.1]
  def change
    # Add new pet_owner column
    add_column :users, :pet_owner, :string

    # Change role column to string
    change_column :users, :role, :string

    # Update existing integer roles to their string equivalents
    reversible do |dir|
      dir.up do
        User.reset_column_information
        User.find_each do |user|
          case user[:role].to_i
          when 0
            user.update_column(:role, 'user')
          when 1
            user.update_column(:role, 'admin')
          when 2
            user.update_column(:role, 'pet_owner')
          end
        end
      end

      dir.down do
        User.reset_column_information
        User.find_each do |user|
          case user[:role]
          when 'user'
            user.update_column(:role, 0)
          when 'admin'
            user.update_column(:role, 1)
          when 'pet_owner'
            user.update_column(:role, 2)
          end
        end
      end
    end
  end
end
