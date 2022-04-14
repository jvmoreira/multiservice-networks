import React, { ReactElement, useEffect } from 'react';
import { StateUpdater } from '@/commons/change-handler';
import { useNfvTeFunctionParameters } from '@/commons/nfv-te-values';
import { SingleRateThreeColorIntervalField } from './single-rate-three-color-interval-field';
import { SingleRateThreeColorBucketFSizeField } from './single-rate-three-color-bucket-f-size-field';
import { SingleRateThreeColorBucketFMaxSizeField } from './single-rate-three-color-bucket-f-max-size-field';
import { SingleRateThreeColorBucketSSizeField } from './single-rate-three-color-bucket-s-size-field';
import { SingleRateThreeColorBucketSMaxSizeField } from './single-rate-three-color-bucket-s-max-size-field';
import { SingleRateThreeColorRateField } from './single-rate-three-color-rate-field';

type SingleRateThreeColorParameters = {
  rate: string,
  bucketF_size: string,
  bucketF_max_size: string,
  bucketS_size: string,
  bucketS_max_size: string,
  interval: string,
};

export function SingleRateThreeColorParameters(): ReactElement {
  const [
    singleRateThreeColorParameters,
    setSingleRateThreeColorParameters,
  ] = useNfvTeFunctionParameters<SingleRateThreeColorParameters>();

  useSetSingleRateThreeColorInitialParameters(setSingleRateThreeColorParameters);

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
