# Crosswalk Assistive Robot Powered by Image Classification

### Project Overview
The crosswalk assistive robot helps blind individuals safely cross by conveying crosswalk conditions through image classification of images, such as crossing and stop signals

## Phase 1: Multiclass Image Classification
Deep CNN model for multiclass classification

### Stages of crossing a crosswalk
- Find a crosswalk (Stop, wait behind the line), crosswalk images
- Stop (Don't proceed to cross), stop signal
- Crossing (Proceed to cross), crossing signal
- End of crosswalk (It’s the end of the crosswalk; watch out for the sudden curb), tactile paving and non tactil paving crosswalk or curb

### Used Python Libraries
### Next steps
- Use VScode (just check if VScode can run multi languages)
- Use laptop speaker to tell the conditions, play recorded audio

**Key hardware components**: Arduino
### Constraints
-  Because I don’t have a camera that can be attached to the robot, I can only use images for training and testing

### Possible further improvements
- If a camera is used, I can process a sequence of frames (video) to inform individuals about the conditions of a crosswalk
