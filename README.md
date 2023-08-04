# Jitsi Extension

Host a Jitsi meeting with a chatBot that allows participants to send funds to each other. 
Each participant is given an LNBits wallet. Any participant can then send funds to any other participant.

## Setup

- Add the following line to your LNBits extension manifest's `repo` section.

```json
{
    "id": "jitsi",
    "organisation": "lnbits",
    "repository": "jitsi"
}
```

- Create or log into your Jaas account at <https://jaas.8x8.vc/> to obtain the following:
  - An application ID.
    
    ![image](https://github.com/nochiel/lnbits-jitsi-extension/assets/284914/bc074cca-605d-44cb-b65d-165ed83811a0)

  - A JWT security token.
    
    ![image](https://github.com/nochiel/lnbits-jitsi-extension/assets/284914/b7247c76-20e1-48a8-bd5a-92c70c1bec2c)


## Usage

- Log into LNbits and enable the Jitsi extension.
- Select the Jitsi extension from the sidebar menu.
- Enter the configuration tokens obtained from Jaas.

  ![image](https://github.com/nochiel/lnbits-jitsi-extension/assets/284914/2fb2fca6-b16c-4b77-a8fd-d95f5e1543bb)

- When you start an Jitsi conference call using LNbits, note that the chat bot runs as you, the host of the meeting.
- In the "Join Meeting" dialog, enter the name *ChatBot*.
    - If you want to participate in the meeting, you should join as a different user. You can name the host user *ChatBot*, for example.
- Note that if the *ChatBot* participant (the hosting LNbits user), types in chat commands, they will not run, which is, again, why you should join the conference call as a different user and not as the *ChatBot*. 
- When a participant joins the meeting, they receive a chat message that tells them their LNBits wallet url and current balance.
- As a participant, type `/help` to view available chatbot commands.

