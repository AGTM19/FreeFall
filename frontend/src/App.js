import React from 'react';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import ProTip from './ProTip';
import {makeStyles} from "@material-ui/core/styles";
import AddIcon from '@material-ui/icons/Add';



const useStyles = makeStyles(theme => ({
  parachutesCard: {
        marginLeft: theme.spacing(1),
        height: 200,
        width: 100,
        background: 'white'
  },
  containerbg: {
    backgroundColor: 'rgb(247,247,247)',
    borderRadius: 10,
    height: 300,
      padding: 20
  },
}));

function ParachuteDiv() {
  const classes = useStyles();
  return (
      <div>
        <h1>Parachutes:</h1>
        <div className={classes.containerbg}>
          <Button color="primary" className={classes.parachutesCard}>
              <div>
                  <AddIcon/>
              </div>
          </Button>
        </div>
      </div>
  );
}

function PlotDiv() {
  const classes = useStyles();
  return (
      <div>
        <h1>Plots:</h1>
        <div className={classes.containerbg}>
        </div>
      </div>
  );
}

export default function App() {
  return (
    <Container maxWidth="sm">
      <Box my={4}>
        <Typography variant="h4" component="h1" gutterBottom>
          Parachute Solver
        </Typography>
        <ParachuteDiv />
        <PlotDiv />
      </Box>
    </Container>
  );
}
