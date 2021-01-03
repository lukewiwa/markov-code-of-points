#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { MarkovCodeOfPointsCdkStack } from '../lib/markov-code-of-points-cdk-stack';

const app = new cdk.App();
new MarkovCodeOfPointsCdkStack(app, 'MarkovCodeOfPointsCdkStack');
