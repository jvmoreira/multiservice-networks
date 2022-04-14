import React, { ReactElement, useEffect, useMemo } from 'react';
import { StateUpdater } from '@/commons/change-handler';
import { useNfvTeFunctionParameters } from '@/commons/nfv-te-values';
import { SingleRateThreeColorIntervalField } from './single-rate-three-color-interval-field';
import { SingleRateThreeColorBucketFSizeField } from './single-rate-three-color-bucket-f-size-field';
import { SingleRateThreeColorBucketFMaxSizeField } from './single-rate-three-color-bucket-f-max-size-field';
import { SingleRateThreeColorBucketSSizeField } from './single-rate-three-color-bucket-s-size-field';
import { SingleRateThreeColorBucketSMaxSizeField } from './single-rate-three-color-bucket-s-max-size-field';
import { SingleRateThreeColorRateField } from './single-rate-three-color-rate-field';
import { SingleRateThreeColorColorAwareField } from './single-rate-three-color-color-aware-field';
import { SingleRateThreeColorCaBucketFSizeField } from './single-rate-three-color-ca-bucket-f-size-field';
import { SingleRateThreeColorCaBucketFMaxSizeField } from './single-rate-three-color-ca-bucket-f-max-size-field';
import { SingleRateThreeColorCaBucketSSizeField } from './single-rate-three-color-ca-bucket-s-size-field';
import { SingleRateThreeColorCaBucketSMaxSizeField } from './single-rate-three-color-ca-bucket-s-max-size-field';
import { SingleRateThreeColorCaRateField } from './single-rate-three-color-ca-rate-field';

type SingleRateThreeColorParameters = {
  rate: string,
  bucketF_size: string,
  bucketF_max_size: string,
  bucketS_size: string,
  bucketS_max_size: string,
  interval: string,
  color_aware?: string,
  ca_bucketF_size?: string,
  ca_bucketF_max_size?: string,
  ca_bucketS_size?: string,
  ca_bucketS_max_size?: string,
  ca_rate?: string,
};

export function SingleRateThreeColorParameters(): ReactElement {
  const [
    singleRateThreeColorParameters,
    setSingleRateThreeColorParameters,
  ] = useNfvTeFunctionParameters<SingleRateThreeColorParameters>();

  useSetSingleRateThreeColorInitialParameters(setSingleRateThreeColorParameters);

  const isColorAwareEnabled = useMemo(() => {
    return singleRateThreeColorParameters.color_aware;
  }, [singleRateThreeColorParameters]);

  useDeleteColorAwareParametersWhenDisabled(isColorAwareEnabled, setSingleRateThreeColorParameters);

  return (
    <>
      <SingleRateThreeColorBucketFSizeField
        singleRateThreeColorParameters={singleRateThreeColorParameters}
        setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
      />

      <SingleRateThreeColorBucketFMaxSizeField
        singleRateThreeColorParameters={singleRateThreeColorParameters}
        setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
      />
      <SingleRateThreeColorBucketSSizeField
        singleRateThreeColorParameters={singleRateThreeColorParameters}
        setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
      />

      <SingleRateThreeColorBucketSMaxSizeField
        singleRateThreeColorParameters={singleRateThreeColorParameters}
        setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
      />

      <SingleRateThreeColorIntervalField
        singleRateThreeColorParameters={singleRateThreeColorParameters}
        setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
      />

      <SingleRateThreeColorRateField
        singleRateThreeColorParameters={singleRateThreeColorParameters}
        setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
      />

      <SingleRateThreeColorColorAwareField
        singleRateThreeColorParameters={singleRateThreeColorParameters}
        setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
      />

      {isColorAwareEnabled && <>
        <SingleRateThreeColorCaBucketFSizeField
          singleRateThreeColorParameters={singleRateThreeColorParameters}
          setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
        />

        <SingleRateThreeColorCaBucketFMaxSizeField
          singleRateThreeColorParameters={singleRateThreeColorParameters}
          setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
        />

        <SingleRateThreeColorCaBucketSSizeField
          singleRateThreeColorParameters={singleRateThreeColorParameters}
          setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
        />

        <SingleRateThreeColorCaBucketSMaxSizeField
          singleRateThreeColorParameters={singleRateThreeColorParameters}
          setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
        />

        <SingleRateThreeColorCaRateField
          singleRateThreeColorParameters={singleRateThreeColorParameters}
          setSingleRateThreeColorParameters={setSingleRateThreeColorParameters}
        />
      </>}
    </>
  );
}

export interface SingleRateThreeColorParameterFieldProps {
  singleRateThreeColorParameters: SingleRateThreeColorParameters,
  setSingleRateThreeColorParameters: StateUpdater<SingleRateThreeColorParameters>,
}

function useSetSingleRateThreeColorInitialParameters(
  setSingleRateThreeColorParameters: StateUpdater<SingleRateThreeColorParameters>,
): void {
  useEffect(() => {
    setSingleRateThreeColorParameters({
      rate: '',
      bucketF_size: '',
      bucketF_max_size: '',
      bucketS_size: '',
      bucketS_max_size: '',
      interval: '',
    });
  }, [setSingleRateThreeColorParameters]);
}

function useDeleteColorAwareParametersWhenDisabled(
  isColorAwareEnabled: SingleRateThreeColorParameters['color_aware'],
  setSingleRateThreeColorParameters: StateUpdater<SingleRateThreeColorParameters>,
): void {
  useEffect(() => {
    if(!isColorAwareEnabled) {
      setSingleRateThreeColorParameters(currentParameters => {
        delete currentParameters.ca_bucketF_size;
        delete currentParameters.ca_bucketF_max_size;
        delete currentParameters.ca_bucketS_size;
        delete currentParameters.ca_bucketS_max_size;
        delete currentParameters.ca_rate;
        return currentParameters;
      });
    }
  }, [isColorAwareEnabled, setSingleRateThreeColorParameters]);
}
