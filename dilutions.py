#!/usr/bin/python
import csv

# Get user input for dilution factor, number of replicates, and final volume of replicates
assay = input("Enter the assay, Y42 or Y77: ")
date = input("Enter the date in DDMMMYYYY: ")
coral_id = input("Enter the Coral ID: ")
dilution_factor = input("Enter dilution factor: ")



if assay == 'Y42':
    vol_sample = input("Enter Volume of Sample, usually use 10-15uL: ")
    dilution_factor = int(dilution_factor)*2
    num_replicates = input("Enter number of final replicates: ")
    final_volume = input("Enter final volume of replicates (in uL): ")
    total_volume = 600
    # Create dilution scheme list
    step1_dilution_factor = int(total_volume)/int(vol_sample)
    dilution_scheme = [(int(vol_sample), 600 - int(vol_sample), "1/{}: {}uL sample + {}uL a.d.".format(step1_dilution_factor, int(vol_sample), 600 - int(vol_sample)))]


    # Step 2 Dilution  
    step2_dilution_factor = (int(dilution_factor)/int(step1_dilution_factor))/2
    print(F"step2 dilution factor = {step2_dilution_factor}, {dilution_factor}/{step1_dilution_factor}")

    vol_prev_dilution = int(total_volume)/int(step2_dilution_factor)
    print(F" vol_prev_dilution = {vol_prev_dilution}, {total_volume}/{step2_dilution_factor}")

    vol_diluent = int(total_volume) - int(vol_prev_dilution)
    print(F"vol_diluent = {vol_diluent}, {total_volume, vol_prev_dilution}")

    instruction = "1/{}: {}uL prev. dilution + {}uL a.d.".format(step2_dilution_factor, int(total_volume)/int(step2_dilution_factor), int(total_volume) - int(vol_prev_dilution))
    dilution_scheme.append((vol_prev_dilution, vol_diluent, instruction))


    # Add final dilution step with replicates
    dilution_factor *= 2
    vol_prev_dilution = 300
    vol_diluent = 300
    instruction = "1/2 Serial Dilution: {}uL prev. dilution + {}uL a.d.".format(vol_prev_dilution, vol_diluent)
    dilution_scheme.append((vol_prev_dilution, vol_diluent, instruction))

    final_instruction = "replicates = {}, {}uL each".format(num_replicates, final_volume)
    dilution_scheme.append(("N/A", final_volume, final_instruction))

    # Write dilution scheme to CSV file
    with open(F'coral{coral_id}_{assay}_dilution_scheme_{date}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Step #", "Instructions", "Dilution Factor"])
        for i, step in enumerate(dilution_scheme):
            # writer.writerow(["Step {}".format(i+1), step[2], step[0] / int(step[1])])
                if i == 0:
                    writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor])
                elif i == 1:
                    writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor * step2_dilution_factor])
                elif i == 2:
                    writer.writerow(["Step {}".format(i+1), step[2], 2 * step1_dilution_factor * step2_dilution_factor])
                else:
                    writer.writerow(["Step {}".format(i+1), step[2], 2 * step1_dilution_factor * step2_dilution_factor])
elif assay == 'Y77':
    vol_sample = input("Enter Volume of Sample, usually use 30-60uL: ")
    dilution_factor = int(dilution_factor)
    total_volume = 600
    # Create dilution scheme list
    step1_dilution_factor = int(total_volume)/int(vol_sample)
    dilution_scheme = [(int(vol_sample), 600 - int(vol_sample), "1/{}: {}uL sample + {}uL a.d.".format(step1_dilution_factor, int(vol_sample), 600 - int(vol_sample)))]


    if vol_sample == 30:
        
        # Step 2 Dilution  
        step2_dilution_factor = 50

        vol_prev_dilution = int(total_volume)/int(step2_dilution_factor)

        vol_diluent = int(total_volume) - int(vol_prev_dilution)

        instruction = "1/{}: {}uL prev. dilution + {}uL a.d.".format(step2_dilution_factor, int(total_volume)/int(step2_dilution_factor), int(total_volume) - int(vol_prev_dilution))
        dilution_scheme.append((vol_prev_dilution, vol_diluent, instruction))

        # Step 3 Dilution  
        step3_dilution_factor = 100

        vol_prev_dilution = int(total_volume)/int(step3_dilution_factor)


        vol_diluent = int(total_volume) - int(vol_prev_dilution)

        instruction = "1/{}: {}uL prev. dilution + {}uL a.d.".format(step2_dilution_factor, int(total_volume)/int(step2_dilution_factor), int(total_volume) - int(vol_prev_dilution))
        dilution_scheme.append((vol_prev_dilution, vol_diluent, instruction))


        with open(F'coral{coral_id}_{assay}_dilution_scheme_{date}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Step #", "Instructions", "Dilution Factor"])
            for i, step in enumerate(dilution_scheme):
                # writer.writerow(["Step {}".format(i+1), step[2], step[0] / int(step[1])])
                    if i == 0:
                        writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor])
                    elif i == 1:
                        writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor * step2_dilution_factor])
                    elif i == 2:
                        writer.writerow(["Step {}".format(i+1), step[2], step2_dilution_factor * step3_dilution_factor])
                    else:
                        writer.writerow(["Step {}".format(i+1), step[2], step2_dilution_factor * step3_dilution_factor])
    elif vol_sample ==60:
         # Step 2 Dilution  
        step2_dilution_factor = 100

        vol_prev_dilution = int(total_volume)/int(step2_dilution_factor)

        vol_diluent = int(total_volume) - int(vol_prev_dilution)

        instruction = "1/{}: {}uL prev. dilution + {}uL a.d.".format(step2_dilution_factor, int(total_volume)/int(step2_dilution_factor), int(total_volume) - int(vol_prev_dilution))
        dilution_scheme.append((vol_prev_dilution, vol_diluent, instruction))



        with open(F'coral{coral_id}_{assay}_dilution_scheme_{date}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Step #", "Instructions", "Dilution Factor"])
            for i, step in enumerate(dilution_scheme):
                # writer.writerow(["Step {}".format(i+1), step[2], step[0] / int(step[1])])
                    if i == 0:
                        writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor])
                    elif i == 1:
                        writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor * step2_dilution_factor])
                    else:
                        writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor * step2_dilution_factor])
         
    else: 
         # Create dilution scheme list
        step1_dilution_factor = int(total_volume)/int(vol_sample)
        dilution_scheme = [(int(vol_sample), 600 - int(vol_sample), "1/{}: {}uL sample + {}uL a.d.".format(step1_dilution_factor, int(vol_sample), 600 - int(vol_sample)))]


        # Step 2 Dilution  
        step2_dilution_factor = (int(dilution_factor)/int(step1_dilution_factor))/2
        print(F"step2 dilution factor = {step2_dilution_factor}, {dilution_factor}/{step1_dilution_factor}")

        vol_prev_dilution = int(total_volume)/int(step2_dilution_factor)
        print(F" vol_prev_dilution = {vol_prev_dilution}, {total_volume}/{step2_dilution_factor}")

        vol_diluent = int(total_volume) - int(vol_prev_dilution)
        print(F"vol_diluent = {vol_diluent}, {total_volume, vol_prev_dilution}")

        instruction = "1/{}: {}uL prev. dilution + {}uL a.d.".format(step2_dilution_factor, int(total_volume)/int(step2_dilution_factor), int(total_volume) - int(vol_prev_dilution))
        dilution_scheme.append((vol_prev_dilution, vol_diluent, instruction))


        instruction = "1/{}: {}uL prev. dilution + {}uL a.d.".format(step2_dilution_factor, int(total_volume)/int(step2_dilution_factor), int(total_volume) - int(vol_prev_dilution))
        dilution_scheme.append((vol_prev_dilution, vol_diluent, instruction))


        # Write dilution scheme to CSV file
        with open(F'coral{coral_id}_{assay}_dilution_scheme_{date}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Step #", "Instructions", "Dilution Factor"])
            for i, step in enumerate(dilution_scheme):
                # writer.writerow(["Step {}".format(i+1), step[2], step[0] / int(step[1])])
                    if i == 0:
                        writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor])
                    elif i == 1:
                        writer.writerow(["Step {}".format(i+1), step[2], step1_dilution_factor * step2_dilution_factor])
                    elif i == 2:
                        writer.writerow(["Step {}".format(i+1), step[2], 2 * step1_dilution_factor * step2_dilution_factor])
                    else:
                        writer.writerow(["Step {}".format(i+1), step[2], 2 * step1_dilution_factor * step2_dilution_factor])
         
else: 
    print("Please try again, as of right now only have schemes for Y77 and Y42")

